from ultralytics import YOLO

def main():
    print("🚀 开始训练基线模型...")
    model = YOLO('yolov8n.pt')
    results = model.train(data='data.yaml', epochs=100, imgsz=640, device=0)
    print("✅ 训练完成，权重已保存。")

if __name__ == '__main__':
    main()