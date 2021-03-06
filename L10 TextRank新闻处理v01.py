#-*- encoding:utf-8 -*-

from textrank4zh import TextRank4Keyword, TextRank4Sentence
import jieba

text = '''10月28日，国新办就“十三五”卫生健康改革发展有关情况举行发布会。国家卫生健康委员会党组成员、副主任于学军表示，从2015年到2019年底，我国居民人均预期寿命从76.3岁提高到77.3岁。2019年二孩及以上孩次占比为59.5%。

　　于学军表示，从2015年到2019年底，我国居民人均预期寿命从76.3岁提高到77.3岁，也就是说4年提高了1岁。孕产妇死亡率、婴儿死亡率、5岁以下儿童死亡率分别从20.1/10万、8.1‰、10.7‰降至17.8/10万、5.6‰、7.8‰，主要健康指标总体上优于中高收入国家平均水平，个人卫生支出占卫生总费用的比重降至28.4%，健康中国建设取得良好开局。

　　于学军表示，妇幼保健和计划生育服务管理继续加强，积极推进健康老龄化。有序调整完善生育政策，2019年二孩及以上孩次占比为59.5%。同时完善相关配套政策，促进3岁以下婴幼儿照护服务发展。全面加强出生缺陷综合防治，开展五类残疾儿童筛查、诊断和康复试点工作。加强老年健康教育和预防保健，大力发展医养结合，为居家老人提供医疗服务的机构达到4万多家，每年免费为65岁以上老人进行健康体检。

　　此外，医疗卫生服务体系不断完善，服务可及性不断提高。优化医疗资源配置，启动国家医学中心和区域医疗中心建设，完善县域医疗卫生服务体系，84%的县级医院达到二级及以上医院水平。从2015—2019年，每万人全科医生数从1.38人增长到2.61人，每千人口医疗卫生机构床位数从5.11张增长到6.3张，执业(助理)医师数从2.22人增长到2.77人，注册护士数从2.37人增长到3.18人。近90%的家庭15分钟内能够到达最近医疗点。

　　此次中国人均预期寿命增加近1岁，人均预期寿命的延长见证了“十三五”时期我国医疗卫生体系的不断提升。这也是新时代特色社会主义制度的功劳吧。
'''

# 输出关键词，设置文本小写，窗口为2
tr4w = TextRank4Keyword()
tr4w.analyze(text=text, lower=True, window=3)
print('关键词：')
for item in tr4w.get_keywords(10, word_min_len=2):
    print(item.word, item.weight)


# 输出重要的句子
tr4s = TextRank4Sentence()
tr4s.analyze(text=text, lower=True, source = 'all_filters')
print('重要性较高的三个句子：')
# 重要性较高的三个句子
for item in tr4s.get_key_sentences(num=3):
    # index是语句在文本中位置，weight表示权重
    print(item.index, item.weight, item.sentence)
print('\n')
print('摘要：')    
for item in sorted(tr4s.get_key_sentences(num=3), key = lambda i: i['index']):
    # index是语句在文本中位置，weight表示权重
    print(item.sentence+'。')
