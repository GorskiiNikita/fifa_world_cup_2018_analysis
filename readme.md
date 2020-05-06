В данной работе рассматриваются данные записей футбольных матчей с чемпионата мира 2018 года в России.<br>
Данные содержатся в 4 csv файлах: FIFAWorldCup2018Matches.csv, FIFAWorldCup2018Lineups.csv, FIFAWorldCup2018Passes.csv и FIFAWorldCup2018Shots.csv<br>


Поля из файла FIFAWorldCup2018Matches.csv:<br>
match_id - Идентификатор матча<br>
match_date - Дата проведения матча<br>
kick_off - Время начального удара<br>
competition_stage_id - Идентификатор стадии соревнований<br>
competition_stage_name - Название стадии соревнования (Group Stage, Round of 16, Quarter-finals, Semi-finals, 3rd Place Final, Final)<br>
home_team_id - Идентификатор первой команды<br>
home_team_name - Название первой команды<br>
home_team_group - Группа первой команды<br>
away_team_id - Идентификатор второй команды<br>
away_team_name - Название второй команды<br>
away_team_group - Группа второй команды<br>
stadium_id - Идентификатор стадиона<br>
stadium_name - Название стадиона<br>
referee_id - Идентификатор главного судьи<br>
referee_name - Имя главного судьи<br>
home_score - Число голов первой команды в основное время<br>
away_score - Число голов второй команды в основное время<br><br>


Поля из файла FIFAWorldCup2018Lineups.csv:<br>
match_id - Идентификатор матча<br>
team_id - Идентификатор команды<br>
team_name - Название команды<br>
player_id - Идентификатор игрока<br>
player_name - Имя игрока<br>
player_nickname - Сокращенное имя игрока<br>
jersey_number - Номер на футболке игрока<br><br>


Поля из файла FIFAWorldCup2018Passes.csv:<br>
match_id - Идентификатор матча<br>
index - Индекс события (в рамках одного матча события упорядочены по этому полю)<br>
id - Уникальный идентификатор события<br>
period - Тайм<br>
minute - Минута<br>
second - Секунда<br>
location_x - Координата x (здесь и далее координаты отсчитываются от левого верхнего угла нарисованного поля в ярдах, один ярд равен 0.915 метра)<br>
location_y - Координата y<br>
team_id - Идентификатор команды<br>
team_name - Название команды<br>
player_id - Идентификатор игрока<br>
player_name - Имя игрока<br>
recipient_id - Идентификатор игрока, которому предназначалась передача<br>
recipient_name - Имя игрока, которому предназначалась передача<br>
end_location_x - Координата x точки, в которую направлялся мяч<br>
end_location_y - Координата y точки, в которую направлялся мяч<br>
length - Длина паса в ярдах<br>
angle - Направление паса в радианах (от −π до π, угол 0 соответствует направлению «вперёд», положительные значения отсчитываются по часовой стрелке)<br>
shot_assist - 1, если передача привела к удару по воротам<br>
goal_assist - 1, если передача привела к голу<br>
assisted_shot_id - Идентификатор удара по воротам, к которому привела передача (в файле FIFAWorldCup2018Shots.csv )<br>
outcome_id - Идентификатор ситуации, к которой привела передача<br>
outcome_name - Название ситуации, к которой привела передача (Incomplete: не дошла, Out: вышла в аут, Pass Offside: пас вне игры, Injury Clearance: мяч выбит из-за травмы, Unknown: неизвестно, если отсутствует, то пас успешный)<br><br>


Поля из файла FIFAWorldCup2018Shots.csv:<br>
match_id - Идентификатор матча<br>
index - Индекс события (в рамках одного матча события упорядочены по этому полю)<br>
id - Уникальный идентификатор события<br>
period - Тайм<br>
minute - Минута<br>
second - Секунда<br>
location_x - Координата x<br>
location_y - Координата y<br>
team_id - Идентификатор команды<br>
team_name - Название команды<br>
player_id - Идентификатор игрока<br>
player_name - Имя игрока<br>
end_location_x - Координата x точки, в которой оказался мяч<br>
end_location_y - Координата y точки, в которой оказался мяч<br>
end_location_z - Координата z точки, в которой оказался мяч (если мяч попадает в ворота, то можно узнать, в верхний или нижний угол был удар, скажем)<br>
key_pass_id - Идентификатор передачи, которая привела к удару<br>
outcome_id - Идентификатор ситуации, к которой привел удар<br>
outcome_name - Ситуация, к которой привел удар (Off T: мимо, Blocked: заблокировали, Saved: вратарь взял, Goal: гол, Wayward: очень неточно, Post: штанга)<br>