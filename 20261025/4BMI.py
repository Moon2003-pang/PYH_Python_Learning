weight = float(input("请输入体重，单位千克:"))
height = float(input("请输入身高，单位米:"))

BMI = weight/(height**2)
print("你的BMI指数为："+str(BMI))