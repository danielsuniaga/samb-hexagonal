import logging

from decouple import config

logger_persistence = logging.getLogger('ServicesPersistence')


class PersistenceLifecycleLogger:

    @staticmethod
    def account_label(mode=None, account_id=None):
        if mode is True:
            return 'REAL'
        if mode is False:
            return 'PRACTICE'
        if isinstance(mode, str) and mode.strip():
            upper = mode.strip().upper()
            if upper == 'REAL':
                return 'REAL'
            if upper in ('PRACTICE', 'DEMO'):
                return 'PRACTICE'
            return mode.strip()
        if account_id not in (None, '', 'N/A'):
            return str(account_id)
        return 'N/A'

    @staticmethod
    def project_name(project=None):
        return project or config('PROJECT_NAME', default='N/A')

    @staticmethod
    def _log(stage, level='info', **fields):
        parts = [f"🔄 PERSISTENCE LIFECYCLE | stage: {stage}"]
        for key, value in fields.items():
            if value is not None:
                parts.append(f"{key}: {value}")
        message = ' | '.join(parts)
        if level == 'error':
            logger_persistence.error(message)
        else:
            logger_persistence.info(message)

    @staticmethod
    def extract_from_payload(payload):
        if not isinstance(payload, dict):
            return 'N/A', 'N/A', 'N/A'
        details = payload.get('contract_details', {}) or {}
        contract_id = details.get('contract_id', 'N/A')
        account = PersistenceLifecycleLogger.account_label(
            payload.get('mode'),
            details.get('account_id', details.get('account_id_broker')),
        )
        methodology = payload.get('id_methodology', 'N/A')
        return contract_id, account, methodology

    @staticmethod
    def broker_close_received(
        contract_id,
        account,
        broker_profit,
        broker_exec_id=None,
        methodology='N/A',
        project=None,
        close_status=None,
    ):
        fields = {
            'Project': PersistenceLifecycleLogger.project_name(project),
            'Methodology': methodology or 'N/A',
            'Contract ID': contract_id,
            'Account': account,
            'Broker Profit': broker_profit,
        }
        if broker_exec_id:
            fields['BrokerExec'] = broker_exec_id
        if close_status:
            fields['Close Status'] = close_status
        PersistenceLifecycleLogger._log('BROKER_CLOSE_RECEIVED', **fields)

    @staticmethod
    def entry_attempt(contract_id, account, methodology, project=None, stake=None, cronjob_id=None):
        fields = {
            'Project': PersistenceLifecycleLogger.project_name(project),
            'Methodology': methodology or 'N/A',
            'Contract ID': contract_id,
            'Account': account,
        }
        if stake is not None:
            fields['Stake'] = stake
        if cronjob_id:
            fields['Cronjob ID'] = cronjob_id
        PersistenceLifecycleLogger._log('ENTRY_ATTEMPT', **fields)

    @staticmethod
    def entry_success(contract_id, account, methodology, entry_id, project=None):
        PersistenceLifecycleLogger._log(
            'ENTRY_SUCCESS',
            Project=PersistenceLifecycleLogger.project_name(project),
            Methodology=methodology or 'N/A',
            **{'Contract ID': contract_id, 'Account': account, 'Entry ID': entry_id},
        )

    @staticmethod
    def entry_failed(contract_id, account, methodology, error, project=None, entry_id=None):
        fields = {
            'Project': PersistenceLifecycleLogger.project_name(project),
            'Methodology': methodology or 'N/A',
            'Contract ID': contract_id,
            'Account': account,
            'Error': error,
        }
        if entry_id:
            fields['Entry ID'] = entry_id
        PersistenceLifecycleLogger._log('ENTRY_FAILED', level='error', **fields)

    @staticmethod
    def entry_skipped(contract_id, account, methodology, skip_reason, project=None, error=None):
        fields = {
            'Project': PersistenceLifecycleLogger.project_name(project),
            'Methodology': methodology or 'N/A',
            'Contract ID': contract_id,
            'Account': account,
            'Skip Reason': skip_reason,
        }
        if error:
            fields['Error'] = error
        PersistenceLifecycleLogger._log('ENTRY_SKIPPED', **fields)

    @staticmethod
    def result_attempt(contract_id, account, methodology, project=None, result_value=None):
        fields = {
            'Project': PersistenceLifecycleLogger.project_name(project),
            'Methodology': methodology or 'N/A',
            'Contract ID': contract_id,
            'Account': account,
        }
        if result_value is not None:
            fields['Result'] = result_value
        PersistenceLifecycleLogger._log('RESULT_ATTEMPT', **fields)

    @staticmethod
    def result_success(contract_id, account, methodology, result_id, result_value, win, project=None, entry_id=None):
        fields = {
            'Project': PersistenceLifecycleLogger.project_name(project),
            'Methodology': methodology or 'N/A',
            'Contract ID': contract_id,
            'Account': account,
            'Result ID': result_id,
            'Result': result_value,
            'Win': win,
        }
        if entry_id:
            fields['Entry ID'] = entry_id
        PersistenceLifecycleLogger._log('RESULT_SUCCESS', **fields)

    @staticmethod
    def result_failed(contract_id, account, methodology, error, project=None, result_value=None, entry_id=None):
        fields = {
            'Project': PersistenceLifecycleLogger.project_name(project),
            'Methodology': methodology or 'N/A',
            'Contract ID': contract_id,
            'Account': account,
            'Error': error,
        }
        if result_value is not None:
            fields['Result'] = result_value
        if entry_id:
            fields['Entry ID'] = entry_id
        PersistenceLifecycleLogger._log('RESULT_FAILED', level='error', **fields)

    @staticmethod
    def skip_if_invalid_broker_result(result, project, methodology=None, skip_reason='INVALID_BROKER_RESULT'):
        if result:
            return True
        PersistenceLifecycleLogger.entry_skipped(
            contract_id='N/A',
            account='N/A',
            methodology=methodology,
            skip_reason=skip_reason,
            project=project,
        )
        return False

    @staticmethod
    def wrap_add_entry_persistence(service, result, candles):
        project = service.get_project_name()
        methodology = service.get_id_methodology()

        if not PersistenceLifecycleLogger.skip_if_invalid_broker_result(result, project, methodology):
            return False

        service.set_candles_movements(candles)
        result = service.set_result_positions(result)
        service.set_result_positions_entity(result)
        service.set_candles_positions(candles)
        result = service.add_entrys(result)

        if not result['status']:
            return False

        ok = service.add_indicators_entrys_persistence()
        if not ok:
            contract_id, account, payload_methodology = PersistenceLifecycleLogger.extract_from_payload(result)
            PersistenceLifecycleLogger.entry_skipped(
                contract_id=contract_id,
                account=account,
                methodology=payload_methodology if payload_methodology != 'N/A' else methodology,
                skip_reason='PERSISTENCE_CHAIN_ABORTED',
                project=project,
            )
        return ok
