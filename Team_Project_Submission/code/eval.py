from ultralytics import YOLO

def main():
    print("📊 开始评估 INT8 量化模型精度...")
    model = YOLO("../runs/detect/train-2/weights/best_int8.onnx", task='detect')
    metrics = model.val(data='data.yaml', split='test')
    print(f"✅ 测试集评估完成。mAP50: {metrics.box.map50:.3f}")

if __name__ == '__main__':
    main()