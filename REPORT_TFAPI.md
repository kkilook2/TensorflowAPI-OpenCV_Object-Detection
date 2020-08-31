# TensorflowAPI-OpenCV_Object-Detection
Hello , I'm Kkilook Dev.

report 2020_08_31
#1. Tensorflow Object Detection API 

<개요>

TFAPI으로 학습 -> 학습된 모델 -> OpenCV로딩 -> TFAPI & OpenCV Object Detection 

<DATASET>
  
  Tensorflow Detection Model Zoo -> pretrained model provide
  
  +other DATASETS
  
   -1: PASCAL_VOC (20 Category)
   
   -2: MS COCO (80 Category)
   
   -3: Google OPEN Image (600 Category) 
   
     -- 원하는 데이터 출 가능 --
     
      OIDv4 tool kit -> OPEN Image에서 원하는 category 추출가능
      
      code>> python3 main.py downloader --classes ____class____, ____class____ --type_csv __train/validation/test 中 1__
      
      code>> python3 main.py downloader --classes ____class____, ____class____ --type_csv --multiclass 1 __train/validation/test 中 1__




<DOWNLOAD Tensorflow Object Detection API>
  
  Github : https://github.com/tensorflow/models/tree/master/research/object_detection
  
  
  
  
<TRAINING _ CUSTOM DATASET TRAINING PROCESS>
  
  API는 tf.record & config 설정이 중요 !!
  
    -tf.record() = 대용량 데이터를 직렬화 하는 t.f 고유 방식
    
    -tf.example() = protocol buffer형태로 tf.record()를 구성함
    
                      ->> I/0 처리속도 향상
  
  
<TRAINING PIPELINE CONFIG>
  
  #TRAINING ARCHITECTURE#
  
  1. 학습용 디렉토리 생성 , mkdir new directory for training
  
  2. pretrained된 모델 다운로드 , pretrained model download
  
  3. 라벨맵 생성 , mk Label map
  
  4. 데이터세트를 tf.record()형태로 변환 ,  transform DATASET to TYPE tf.record()
  
  5. pipeline config 수정 
  
  6. 학습 수행 , training start
  
  
  
  <#1 학습용 디렉토리 생성 >
  
  ~/DLCV/Detection/Tensor_api/___new directory name___ (mkdir  director name)
  
  ~/DLCV/Detection/Tensor_api/___new directory name___/ mkdir annotations    <=annotation file(xml, csv) & Lable Map : 학습할떄 필요한 img안에서 obj위치 정보를 담은 파일
  
                                                          "   config         <=
                                                          
                                                          "   pretrained     <=ssd_inception_v2, coco_da
                                                          
                                                          "   training       <=trained data write place : 학습된 데이터 저장, w(가중치)값들
                                                          
                                                          
                                                          
  <#2 pretrained된 모델 다운로드 >
  
  Google : Tensorflow Object Detection Model zoo
  
  __address__ = https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md
  
  cmd : ~DLCV/Detection/Tensor_api/___new directory name___/pretrained/ : wget __address__
  
                                                           /pretrained/ : tar -xvf ssd_inception_v2_coco.tar.gz    : 압축풀기
                                               
                                               
                                                           
  <#3 Label Map 생성 >
  
  -label map download- 
  
  __address__ : https://github.com/tensorflow/models/tree/master/research/object_detection/data /__알맞은 label map. pbtxt__ (raw 주소 복사)
  
 
  cmd : ~DLCV/Detection/Tensor_api/___new directory name____/annotations/ : wget __address__
  
  
  
                                                        
  
  

