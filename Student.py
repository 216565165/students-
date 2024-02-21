import os
from tabulate import tabulate
filename='student.txt'
def main():
    menm()
    while True:

        choice=int(input('请选择:'))
        if choice in[0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer=input('确认退出(y/n):')
                if answer=='y' or answer=='Y':
                    print('已退出')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
        else:
            print('输入错误请重新输入')


def menm():
    print('==============学生管理系统=============')
    print('---------------功能菜单---------------')
    print('\t\t\t1.录入学生信息')
    print('\t\t\t2.查找学生信息')
    print('\t\t\t3.删除学生信息')
    print('\t\t\t4.修改学生信息')
    print('\t\t\t5.排序')
    print('\t\t\t6.统计学生总人数')
    print('\t\t\t7.显示所有学生信息')
    print('\t\t\t0.退出系统')
    print('------------------------------------')


def insert():
    student_list=[]
    while True:
        id=input('请输入ID:')
        if not id:
            break
        name=input('请输入姓名:')
        if not name:
            break
        try:
            english=int(input('请输入英语成绩:'))
            python=int(input('请输入Python成绩:'))
            java=int(input('请输入Java成绩:'))
        except:
            print('成绩无效，重新输入')
            continue
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        student_list.append(student)
        answer=input('是否继续添加y/n\n')
        if answer=='y':
            continue
        else:
            break
    save(student_list)
    print('录入完毕')
def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按ID查找输入1，按姓名查找按2:')
            if mode=='1':
                id=input('请输入ID:')
            elif mode=='2':
                name=input('请输入姓名:')
            else:
                print('输入错误，请重新输入')
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            student_query.append(d)
                        elif name!='':
                            if d['name']==name:
                                student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer=input('是否继续(y/n):')
            if answer=='y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息')
            return

def show_student(lst):
    if len(lst) ==0:
        print('未查询到该学生信息')
        return
    # format_01=open(filename)
    # format_02=[str(format_01)]
    #
    # print(tabulate(format_01, headers='firstrow', tablefmt='fancy_grid'))

    for item in lst:
        print("ID:", format(item.get('id')))
        print("姓名:", format(item.get('name')))
        print("英语成绩:", format(item.get('english')))
        print("Python成绩:", format(item.get('python')))
        print("Java成绩:", format(item.get('java')))
        print("================================================")


def delete():
    while True:
        student_id=input('请要删除的学生ID:')
        if student_id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8')as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f'id为{student_id}的信息已删除')
                    else:
                        print(f'id{student_id}未找到')
            else:
                print('无学生信息')
                break
            show()
            answer=input('是否继续(y/n):')
            if answer=='y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        return
    student_id=input('请输入要修改的学生ID:')
    if student_id != '':
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                student_old = file.readlines()
        else:
            student_old = []
        flag = False
        if student_old:
            with open(filename, 'w', encoding='utf-8') as wfile:
                d = {}
                for item in student_old:
                    d = dict(eval(item))
                    if d['id'] != student_id:
                        wfile.write(str(d) + '\n')
                    else:
                        flag = True
    student_list=[]
    while True:
        id = input('请输入ID:')
        if not id:
            break
        name = input('请输入姓名:')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩:'))
            python = int(input('请输入Python成绩:'))
            java = int(input('请输入Java成绩:'))
        except:
            print('成绩无效，重新输入')
            continue
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        save(student_list)
        break

    # with open(filename,'w',encoding='utf-8') as wfile:
    #     for item in student_id:
    #         continue
    #         d=dict(eval(item))
    #         if d['id'] == student_id:
    #             print('找到学生信息，可以进行修改')
    #             while True:
    #                 try:
    #                     d['name'] = input('请输入姓名:')
    #                     d['english'] = input('请输入英语成绩:')
    #                     d['python'] = input('请输入Python成绩')
    #                     d['java'] = input('请输入Java成绩:')
    #                 except:
    #                     print('输入错误，请重新输入')
    #                 else:
    #                     break
    #             wfile.write(str(d)+'\n')
    #             print('修改成功')
    #         else:
    #             wfile.write(str(d)+'\n')
    answer=input('是否继续修改(y/n)\n')
    if answer=='y':
        modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students_list=rfile.readlines()
        student_new=[]
        for item in students_list:
            d=dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc=input('请选择(0.升序1.降序):')
    if asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('输入有误请重新输入')
        sort()
    mode=input('请选择排序方式:1.英语成绩2.Python成绩3.Java成绩')
    if mode=='1':
        student_new.sort(key=lambda x: int(x['english']),reverse=asc_or_desc_bool)
    elif mode=='2':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode=='3':
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    else:
        print('输入有误请重新输入')
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf8') as rfile:
            students=rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('没有录入学生信息')
    else:
        print('没有保存信息')

def show():
    student_list=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            for item in students:
                student_list.append(eval(item))
            if student_list:
                show_student(student_list)
    else:
        print('没有保存信息')

if __name__ == '__main__':
    main()