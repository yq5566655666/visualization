import tushare as ts

def get_data(code):
    dict_return = {} # 存放需要的数据
    data = ts.get_hist_data(code) # 通过股票代码获取股票最近的数据
    data_30 = data[:30].iloc[::-1] # 按照日期正序排列数据
    data_30['rise'] = data_30['price_change'] > 0 # 涨
    data_30['fall'] = data_30['price_change'] < 0 # 跌
    close = data_30['close'] #最近30个交易日的收盘价
    close_index = list(close.index) # 收盘价x轴数据
    close_value = close.values.tolist() # 收盘价y轴数据
    df_diff = data_30[['rise','fall']].sum() # 统计近30交易日的涨跌次数
    df_diff_index = list(df_diff.index) # 将数据转为列表格式
    df_diff_value = df_diff.values.tolist() # 将数据转为列表格式
    dict_return['diff'] = [{"name":item[0],"value":item[1]} for item in list(zip(df_diff_index,df_diff_value))] # 将数据制作成饼图需要的数据格式
    price_change = data_30['price_change'].values.tolist() # 统计近30交易日的价格变化
    volume = data_30['volume'].values.tolist() # 统计近30交易日的成交量
    # 以下为将处理好的数据加入字典
    dict_return['close_index'] = close_index
    dict_return['close_value'] = close_value
    dict_return['price_change'] = price_change
    dict_return['volume'] = volume
    dict_return['df_diff_index'] = df_diff_index
    return dict_return

# def get_name(code):
#     '''通过股票代码导出公司名称'''
#     pro=ts.pro_api()
#     dat = pro.query('stock_basic', fields='symbol,name')
#     company_name = list(dat.loc[dat['symbol'] == stoke_code].name)[0]
#     return company_name


#get_data('002503')