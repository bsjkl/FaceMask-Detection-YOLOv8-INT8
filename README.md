## TP-5D 轻量级人脸口罩实时检测与预警系统

## 一、项目简介
本项目致力于解决目标检测模型在算力受限的边缘设备（如门禁系统）上的部署难题。基于 YOLOv8n 基线架构，通过 INT8 深度模型量化压制与流媒体内存优化，实现了纯 CPU 环境下高帧率的实时推断与状态机逻辑预警。

## 二、团队成员与分工
| 姓名 | 学号 | 分工 |
| :--- | :--- | :--- |
| 彭义翔 | [2024141450209] | 组长：整体架构设计、核心模型训练、INT8量化压缩工程实现与最终实时系统编写 |
| 王庄煦 | [2024141450181] | 数据集分析预处理、验证集切分与 `data_utils.py` 编写 |
| 黄子琪 | [2024141450194] | 环境依赖测试与配置、辅助数据清洗 |
| 谭瑞 | [2024141450170] | 实验结果图表提取 (`results/` 目录维护)、对比分析 |
| 陈小杰 | [2024141450184] | 撰写 `report.pdf` 实验报告与排版 |

## 三、环境配置
```bash
# Python 版本
Python 3.9+

# 安装依赖包
pip install -r requirements.txt -i [https://pypi.tuna.tsinghua.edu.cn/simple](https://pypi.tuna.tsinghua.edu.cn/simple)

## 四、数据集
* **名称**：自建高清口罩佩戴数据集
* **规模**：包含 1400 张高清图像
* **特点**：涵盖日常光照、遮挡及不同角度的复杂场景。数据集配置文件见项目根目录的 `data.yaml`。

# 1. 数据校验
python code/data_utils.py

# 2. 训练基线模型
python code/train.py

# 3. 执行 INT8 极限压制导出
python code/model.py

# 4. 评估量化模型精度
python code/eval.py

# 5. 交互式流媒体演示 (核心预警系统)
# 可在终端运行或使用 Jupyter 打开 demo.ipynb
python code/demo.py

## 六、实验结果
| 方法 | 综合准确率 (mAP50) | 物理体积 | CPU 实时推理帧率 |
| :--- | :--- | :--- | :--- |
| Baseline (FP32) | 86.5% | 6.0MB | ~30-50 FPS |
| 改进方法 (INT8量化) | 86.5% | **~1.5MB** | **120.6 FPS** |

your-project/
├── code/                  # 源代码目录
│   ├── data_utils.py
│   ├── train.py
│   ├── model.py
│   ├── eval.py
│   └── demo.ipynb
├── report/                # 报告文档
│   └── report.pdf
├── results/               # 实验结果可视化
│   ├── loss_curve.png
│   ├── confusion_matrix.png
│   └── comparison_table.png
├── README.md              # 项目说明
├── requirements.txt       # 依赖列表
└── contribution.txt       # 成员分工声明
