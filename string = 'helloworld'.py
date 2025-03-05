# 定义原始名称列表
names = [
    "InitSMC_WinderDancerSpeedAdapt [FC32081]",
    "InitSMC_WinderIndirectTension [FC32085]",
    "InitSMC_WinderIndirectTensionSpeedAdapt [FC32087]",
    "InitSMC_WinderTensionSpeedAdapt [FC32084]",
    "InitSMC_WinderTensionTorqueAdapt [FC32082]",
    "InitSMC_WinderVconstant [FC32086]",
    "InitSMC_SectionalDancerSpeedAdapt [FC7]",
    "InitSMC_SectionalDrawControl [FC32089]",
    "InitSMC_SectionalIndirectTension [FC10]",
    "InitSMC_SectionalIndirectTensionSpeedAdapt [FC11]",
    "InitSMC_SectionalTensionSpeedAdapt [FC9]",
    "InitSMC_SectionalTensionTorqueAdapt [FC8]",
    "InitSMC_FrictionMeasurement [FC5]",
    "InitSMC_KpAdaptation [FC6]"
]

for name in names:
    # 先删除 InitSMC
    new_name = name.replace("InitSMC_", "")
    # 再删除 [*]
    start_index = new_name.find("[")
    if start_index != -1:
        new_name = new_name[:start_index].strip()

    # 为处理后的名称添加 .txt 扩展名
    file_name = f"{new_name}.txt"

    try:
        # 创建并打开文件以写入模式
        with open(file_name, 'w') as file:
            # 这里可以根据需要写入内容，当前示例为空文件
            pass
        print(f"成功创建文件: {file_name}")
    except Exception as e:
        print(f"创建文件 {file_name} 时出错: {e}")