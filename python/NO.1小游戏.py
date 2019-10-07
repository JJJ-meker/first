print('-'*30,'欢迎来到《孙小猴大战白骨精》','-'*30)

print('请选择你的身份:')
print('\t 1.孙小猴')
print('\t 2.白骨精')
print('-'*82)
player_chocie=input('请选择[1,2]:')
if player_chocie=='1':
    print('你将以->孙小猴<-的身份进行游戏')
elif player_chocie=='2':
    print('你竟然选了->白骨精<-,太不要脸了，系统决定将你的身份定为->孙小猴<-')
else:
    print('对不起，没有这个选项，系统将自动分配你的身份为->孙小猴<-！')

x=2 #生命值
y=2 #攻击力
lv=1 #等级

boss_x=100 #boss生命
boss_y=100 #boss攻击力

print('-'*82)
print(f'孙小猴，你的等级为{lv},你的生命值为{x}，你的攻击力为{y}')
while True:
    print('-'*82)
    print('请选择你要进行的操作:')
    print('\t 1.练级')
    print('\t 2.打boss')
    print('\t 3.逃跑')
    c=input('请选择你要做的操作[1-3]:')
    if c=='1':
        x+=2
        y+=2
        lv+=1
        print('-'*82)
        print(f'孙小猴，恭喜你升级了，你现在的等级为{lv},你的生命值为{x}，你的攻击力为{y}')
    elif c=='2':
        print('->孙小猴<-找到->白骨精<-的洞穴，然后钻入洞中，发现->白骨精<-正准备吃一个和尚，于是他引出->白骨精<-，并攻击了->白骨精<-')
        boss_x-=y
        if boss_x<=0:
            print(f'->白骨精<-受到了{y}点伤害，重伤不治死亡，->孙小猴<-赢得了胜利！GAME OVER')
            break
        x-=boss_y
        print(f'->白骨精<-攻击了->孙小猴<-')
        if x<=0:
            print(f'你受到了{boss_y}点伤害，重伤不治，死亡！GAME OVER')
            break
    elif c=='3':
        print('-'*82)
        print('->孙小猴<-发觉自己打不过->白骨精<-，一扭头，撒腿就跑！->白骨精<-见状，赶上来一巴掌拍死了->孙小猴<-！GAME OVER')
        break
    else:
        print('-'*82)
        print('你的输入有误，请重新输入')
input('回车键退出：')
