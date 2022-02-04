from aiogram.utils.markdown import text
from aiogram.utils.emoji import emojize

kb = {
    'bt_final': ':1234:Рассчитать нужное количество баллов на файнале:1234:',
    'bt_chan': ':family:Полезные группы/каналы в телеграм:family:',
    'bt_sub': ':calendar:Список предметов ИТ по триместрам(актуально на 05.21):calendar:',
    'bt_about': ':bust_in_silhouette:О нас:bust_in_silhouette:',
}
msg = {
    'channels': text(
        emojize(':notebook_with_decorative_cover:Канал со всеми гайдами:\n'),
        emojize('https://t.me/guidebook_aituhelper\n\n'),
        emojize(':page_with_curl:Группа по вопросам по кодингу:\n'),
        emojize('https://t.me/joinchat/IL49QFagCrPWv5cRQ-o_aA\n\n'),
        emojize(':space_invader:Общая флуд беседа:\n'),
        emojize('https://t.me/joinchat/F0QHyE0gUNE3vfz9SFZW3w\n\n'),
        emojize(':gun:Основная беседа военной кафедры:\n'),
        emojize('https://t.me/joinchat/VUhk9IEQjGcXWQwL\n\n'),
        emojize(':mag:Бюро находок:\n'),
        emojize('https://t.me/findAITU\n\n'),
        emojize(':bow:AI 2U:\n'),
        emojize('https://t.me/ait2u\n\n'),
        emojize(':newspaper:AITU news без флуда:\n'),
        emojize('https://t.me/aitu_news\n\n'),
        emojize(':books:Электронная библеотека [БОТ]:\n'),
        emojize('@aitulibrarybot\n\n')),
    '2nd_att': text(
        emojize(':two:Введите баллы за 2-ую половину триместра (2nd Attestation): ')),
    '1nd_att_wrong': 'Неверное число, введите баллы за 1-ую половину триместра (1st Attestation): ',
    '2nd_att_wrong': 'Неверное число, введите баллы за 2-ую половину триместра (2nd Attestation): ',
    'echo_error': 'Я не понял вас, если команда не работает, просто перезапустите бота: /start'

}

misc = {
    'start': ':cyclone:Выберите услугу::cyclone:',
    'calc_start': ':one:Введите баллы за 1-ую половину триместра (1st Attestation): ',
    'subjects': ':page_with_curl:Список предметов::page_with_curl:\n',
    'about': 'По всем вопросам: @operator_aituhelperbot',
    'retake': 'У вас слишком мало баллов по мид тёрмам, вы не допускаетесь на файнал'
}
