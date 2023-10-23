from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from openpyxl import Workbook

from review.models import Review


def export_to_excel(request, pk):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="detail.xlsx"'

    wb = Workbook()
    ws = wb.active
    ws.title = "Опросник"

    headers = [
        'Наименование проверки',
        'Автор',
        'Аудиторское извещение дало Вам разумное количество времени для подготовки к аудиту',
        '''Для Вашего понимания области аудита и целей аудита руководитель аудиторской проверки
                                сформулировал их достаточно ясно при первой встрече с аудиторами или в начале аудита.
                         У Вас была возможность внести свои предложения по выбору вопросов/проектов
                                для аудита, дополнительным задачам аудита.''',
        '''Запросы аудиторов адекватно учитывали текущие задачи Вашего подразделения, 
                                чтобы не оказывать существенного влияния на текущие бизнес-процессы.''',
        "Комментарий Блока A",
        '''Коммуникации и взаимоотношения между Вами и аудиторами во время аудита 
                                были удовлетворительными в целом.''',
        '''Аудиторы показали достаточное понимание бизнеса, бизнес-процессов и внутренней деятельности,
                                чтобы быть в состоянии выполнить аудит''',
        '''Устные рекомендации, данные аудиторами в ходе аудита (если таковые были), 
                                помогли улучшить Ваши методы работы ''',
        'В процессе  аудита с Вами были обсуждены аудиторские обнаружения и результаты аудита',
        "Комментарий Блока B",
        '''Обнаружения в аудиторском отчете точно сформулированы,  
                            предельно ясно и четко объясняют наличие проблемной зоны в системе внутреннего контроля ''',
        '''Рекомендации в аудиторском отчете направлены на снижение рисков и улучшат контроли в
                                бизнес-процессах Вашего подразделения''',
        '''Во время аудита и/или на заключительной встрече, и в любом случае перед 
                                выпуском аудиторского отчета, у Вас была возможность обсудить результаты аудита''',
        '''Сроки устранения аудиторских замечаний в Плане мероприятий были своевременно
                                согласованы и носят комфортный характер для их устранения''',
        "Комментарий Блока C",
        '''Аудиторские цели сосредоточились на ключевых областях риска, 
                                которые есть в Вашем подразделении/бизнес-процессе''',
        '''Независимая оценка внутреннего аудита оказывает положительное влияние на
                                эффективность функционирования системы внутреннего контроля ''',
        'Комментарий Блока D',
        'Общая оценка',
        'Пожелания',
    ]
    ws.append(headers)

    reviews = get_object_or_404(Review, pk=pk)
    ws.append([
        str(reviews.title),
        str(reviews.author),
        reviews.block_a_1,
        reviews.block_a_2,
        reviews.block_a_3,
        str(reviews.comment_block_a),
        reviews.block_b_1,
        reviews.block_b_2,
        reviews.block_b_3,
        reviews.block_b_4,
        str(reviews.comment_block_b),
        reviews.block_c_1,
        reviews.block_c_2,
        reviews.block_c_3,
        reviews.block_c_4,
        str(reviews.comment_block_c),
        reviews.block_d_1,
        reviews.block_d_2,
        str(reviews.comment_block_d),
        reviews.total_for_all_blocks,
        str(reviews.wishes),
    ])

    wb.save(response)
    return response
