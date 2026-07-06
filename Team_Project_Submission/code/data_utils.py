import os
import yaml

def verify_dataset(yaml_path='../data.yaml'):
    print(f"🔍 正在校验数据集配置文件: {yaml_path}")
    if not os.path.exists(yaml_path):
        print("未找到 data.yaml，请检查路径。")
        return
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    print(f"✅ 数据集校验通过。包含类别: {data.get('names', [])}")

if __name__ == '__main__':
    verify_dataset()