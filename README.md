# EvolutionaryEventGraph
Evolutionary Event Graph based on Travel note crawled from XieCheng，基于50W携程出行攻略的顺承事件抽取与事件图谱构建. 

[liuhuanyong/SequentialEventExtration: Sequential Event Experiment based on Travel note crawled from XieCheng，基于50W携程出行游记的采集与顺承事件图谱构建． (github.com)](https://github.com/liuhuanyong/SequentialEventExtration) 

# 项目来源
目前,以谓词性短语作为事件表示的方法方兴未艾,针对特定领域,构建起特定领域的顺承事件图谱,可以支持事件推理,基于事件的意图识别与推荐等多项运用.
本项目将从出行领域展开进行实验.

# 项目构成  
本项目由两个部分的组成,具体包括语料的获取以及基于语料的事件挖掘两个部分,具体项目目录包括:  
news_spider:基于scrapy的游记采集脚本  
event_graph:基于依存句法与顺承模式的顺承事件抽取脚
image:游记顺承事件图谱效果图  

# 一   出行领域语料的获取
1) 语料来源:携程出行攻略    
2) 时间范围:2018年7月14日之前  
3) 采集方式:使用scrapy编写爬虫脚本进行抓取  
4) 采集规模:共采集505767篇，量级50W　　
5) 采集脚本目录:news_spider/travelspider  
6) 语料举例:   

            107330 一路向南——第二篇相逢南通（自驾游） - 游记攻略【携程攻略】
            107331 彩云之南—云上的蜜月之旅 - 丽江游记攻略【携程攻略】
            107332 甘肃游记之玛曲郎木寺 - 碌曲游记攻略【携程攻略】
            107333 拍客白沙行 - 舟山游记攻略【携程攻略】
            107334 九华山-沐浴在佛恩下的XXX - 九华山游记攻略【携程攻略】
            107335 垦丁夏季活动 - 垦丁游记攻略【携程攻略】
            107336 行走在台湾（向隅版）---世外桃源之我们的家（九份民宿） - 九份游记攻略【携程攻略】
            107337 卫赛节马来西亚行 - 马六甲州游记攻略【携程攻略】
            107338 蓝天下的嘉峪关 - 嘉峪关游记攻略【携程攻略】
            107339 人生一定要登一次雪山---都日峰 - 四川游记攻略【携程攻略】
            107340 八月，青海湖不远 - 海北游记攻略【携程攻略】
            107341 #冬季北京# 帝都极冷天去首富的酒店避避寒 - 北京游记攻略【携程攻略】
            107342 圣地西藏 - 青海湖游记攻略【携程攻略】
            107343 孩子，妈妈想让你见识更多的繁华世界 - 深圳游记攻略【携程攻略】
            107344 顶级奢华，舍我其谁！ - 澳门游记攻略【携程攻略】
            107345 旅行、不需要走远！美景就在身边 - 江门游记攻略【携程攻略】
            107346 安安静静，不言不语都是好风景 - 厦门游记攻略【携程攻略】
            107347 邂逅则天故里 行走美丽利州 体验师带你看中国女儿节 - 广元游记攻略【携程攻略】
            107348 台湾，可以这样玩--15日环岛自由行全记录 - 台北游记攻略【携程攻略】
            107349 让我记忆深刻的厦门--详细版 - 厦门游记攻略【携程攻略】
            107350 上海地鐵站 - 上海游记攻略【携程攻略】
            107351 逃离雾霾，带着“马拉多纳”去腾冲 - 腾冲游记攻略【携程攻略】
            107352 在我心上用力地开一 - 四川游记攻略【携程攻略】
            107353 冬季到鄱阳湖边的余干县看鸟，多张美图记录环湖游全过程 - 余干游记攻略【携程攻略】
            107354 2014.十一沈阳，本溪老边沟，枫叶大道，丹东，不走重复路，古迹，景色5日穷游 - 沈阳游记攻略【携程攻略】
            107355 库不齐老牛湾之户外行走 - 库布齐沙漠游记攻略【携程攻略】
        
# 二   基于出行语料的顺承事件图谱构建
# 1, 顺承事件的抽取  
event_extract.py, 思想步骤如下:  
1) 输入游记文本  
2) 对游记进行长句切分  
3) 基于构造的顺承关系模板,进行顺承前后部分提取, 转入4)  
4) 对3)得到的部分进行短句处理,转入5)  
5) 对4)得到的短句进行谓词性短语提取  
6) 对5)得到的谓词性短语向上汇聚,得到一个长句的谓词性短语有序集合  
7) 对6)步骤得到的谓词性短语集合,以滑窗方式构造顺承关系事件对  
8) 对步骤7)得到的顺承事件对进行汇总,最终得到顺承事件库    
9) 对8)进行事件进行整合,去除过低频次的事件,构造标准顺承关系库

# 2, 顺承事件图谱的展示  
10)使用VIS插件进行顺承关系图谱构建与展示, event_graph.py    
11)由于VIS作为一个封装的JS库,因此生成的顺承图谱在项目中暂时设置到500,见travel_event_graph.html  

# 三   顺承关系图谱效果
# 1) 总体图谱样式
以500个顺承事件, 进行顺承事件图谱展示,结果是一张事件网络,这是一个大的顺承关系图谱,由众多小子图谱构成  
![image](https://github.com/liuhuanyong/SequentialEventGraph/blob/master/image/graph.png)
# 2) 去丽江子图谱
该子图谱围绕"去丽江旅游"这一出行事件为核心形成的事件群:
![image](https://github.com/liuhuanyong/SequentialEventGraph/blob/master/image/all.png)
# 3) 飞机路线子图谱 
该子图谱显示了选择飞机进行出行形成的事件序列 
![image](https://github.com/liuhuanyong/SequentialEventGraph/blob/master/image/plane.png)
# 4) 火车路线子图谱
该子图谱显示了选择火车进行出行形成的事件序列
![image](https://github.com/liuhuanyong/SequentialEventGraph/blob/master/image/train.png)
# 5) 订酒店事件图谱
该子图谱描述了一个"预定酒店不愉快事件",从预定到失望到总结,在这条顺承事件链表现出来
![image](https://github.com/liuhuanyong/SequentialEventGraph/blob/master/image/book.png)
# 6) 做饭事件图谱
该子图谱表示了一个"做饭"场景下的顺承事件,感觉也很有意思
![image](https://github.com/liuhuanyong/SequentialEventGraph/blob/master/image/food.png)

# 总结  
1) 该项目只是一个基于50W文章领域语料,运用简单提取方式形成的顺承关系图谱demo,还有很多不足  
2) 该项目目前是形成了事件节点为326781个, 顺承事件对为543580条,分别为30W和50W的图谱规模  
3) 对于谓词性短语进行事件表示是事件表示的一种方式,本方法只采用VOB关系进行提取,这种方式还有待改进  
4) 以3)得到的结果中,还存在大量噪声,这一方面准确率受依存句法的准确性限制,另一方面该依存关系可能还相对单一,不够准确 
5) 在构造顺承事件序列的方法,本项目采用的是长句为单位下的滑窗方式进行构造,这个方式还有待改进  
6) 基于目前形成的顺承关系图谱还有待于进一步挖掘,可以在此基础上完成更多有价值的信息挖掘  


# contact 
如有自然语言处理、知识图谱、事理图谱、社会计算、语言资源建设等问题或合作，请联系我:  
邮箱:lhy_in_blcu@126.com  
csdn:https://blog.csdn.net/lhy2014  
我的自然语言处理项目: https://liuhuanyong.github.io/  
刘焕勇，中国科学院软件研究所  
