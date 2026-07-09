from ultralytics import YOLO 

def export_quantized_model():
    print("⚙️ 开始进行 INT8 模型量化压缩...")
    model = YOLO("../runs/detect/train-2/weights/best.pt")
    model.export(format="onnx", int8=True, data="data.yaml")
    print("✅ 量化模型 best_int8.onnx 导出成功。")

if __name__ == '__main__':
    export_quantized_model()
