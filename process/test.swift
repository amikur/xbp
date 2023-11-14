Privacy - Camera Usage Description"カメラを使用して写真を撮ります"
import UIKit
import AVFoundation

class ViewController: UIViewController {

    @IBOutlet weak var imageView: UIImageView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // カメラの使用許可を取得する
        let cameraAuthorizationStatus = AVCaptureDevice.authorizationStatus(for: AVMediaType.video)
        if cameraAuthorizationStatus == .notDetermined {
            AVCaptureDevice.requestAuthorization(for: AVMediaType.video, completionHandler: { (status) in
                if status == .authorized {
                    // カメラを起動
                    self.startCamera()
                }
            })
        } else if cameraAuthorizationStatus == .authorized {
            // カメラを起動
            self.startCamera()
        }
    }

    func startCamera() {
        // カメラセッションを作成
        let session = AVCaptureSession()

        // バックカメラを取得
        let backCamera = AVCaptureDevice.default(for: AVMediaType.video)

        // バックカメラをセッションに追加
        let input = try! AVCaptureDeviceInput(device: backCamera)
        session.addInput(input)

        // 出力デバイスを作成
        let output = AVCaptureStillImageOutput()
        output.outputSettings = [AVVideoCodecKey: AVVideoCodecJPEG]
        session.addOutput(output)

        // セッションを開始
        session.startRunning()

        // カメラのフレームを取得
        let previewLayer = AVCaptureVideoPreviewLayer(session: session)
        previewLayer.frame = view.bounds
        view.layer.addSublayer(previewLayer)

        // 撮影ボタンを追加
        let captureButton = UIButton(type: .system)
        captureButton.frame = CGRect(x: 0, y: 0, width: 100, height: 50)
        captureButton.center = view.center
        captureButton.setTitle("撮影", for: .normal)
        captureButton.addTarget(self, action: #selector(captureImage), for: .touchUpInside)
        view.addSubview(captureButton)
    }

    @objc func captureImage() {
        // 出力デバイスから画像を取得
        let imageData = output.captureStillImageAsynchronously(completionHandler: { (imageData, error) in
            if let imageData = imageData {
                // 画像をUIImageViewに表示
                let image = UIImage(data: imageData)
                self.imageView.image = image
            }
        })
    }
}
