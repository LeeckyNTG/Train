# 必填
# 用户名
USER_NAME = ''
# 密码
USER_PWD = ''
# 出发站
FROM_STATION = '广州'
# 到达站
TO_STATION = '贵阳'
# 乘车日期（格式: YYYY-mm-dd）
TRAIN_DATE = '2018-12-27'
# 购票人身份证号
PASSENGERS_ID = ['52232119961130762X']
# 票类型（单程:dc 往返:wc）
TOUR_FLAG = 'dc'

# 选填
# 车次 eg:['G6343','G6212']
TRAINS_NO = ['K365']
# 座位类别（商务座(9),特等座(P),一等座(M),二等座(O),高级软卧(6),软卧(4),硬卧(3),软座(2),硬座(1),无座(1)）
SEAT_TYPE_CODE = ['3', '1']
# 购票人类别（成人票:1,儿童票:2,学生票:3,残军票:4）
PASSENGER_TYPE_CODE = '3'
# 座位选择 eg:['1A','2A'],有多少张票就填多少个,其中，A靠窗，B中间，C过道,D过道,F靠窗
CHOOSE_SEATS = []

# 刷票间隔(单位:s)
QUERY_TICKET_REFERSH_INTERVAL = 5
