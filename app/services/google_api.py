from datetime import datetime as dt
from typing import List

from aiogoogle import Aiogoogle

from app.core.config import settings
from app.models import CharityProject
from app.services import constants as const

FORMAT = "%Y/%m/%d %H:%M:%S"


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    now_date_time = dt.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheet_body = {
        'properties': {
            'title': f'{const.SPREDSHEET_REPORT_TITLE} {now_date_time}',
            'locale': const.SPREDSHEET_REPORT_LOCALE
        },
        'sheets': [{'properties': const.SPREDSHEET_SHEET_PROPERTIES}]
    }

    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheet_id = response['spreadsheetId']
    return spreadsheet_id


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.email}
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheetid: str,
        projects: List[CharityProject],
        wrapper_services: Aiogoogle
) -> None:
    now_date_time = dt.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    table_values = [
        ['Отчет от', now_date_time],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ]
    for proj in projects:
        delta = proj.close_date - proj.create_date
        new_row = [proj.name, str(delta), proj.description]
        table_values.append(new_row)

    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    rows_count = len(update_body['values'])
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range=f'A1:C{rows_count}',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
