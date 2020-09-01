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




 < DOWNLOAD Tensorflow Object Detection API >
  
  Github : https://github.com/tensorflow/models/tree/master/research/object_detection
  
  
  
  
 < TRAINING _ CUSTOM DATASET TRAINING PROCESS >
  
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
  
 
  cmd : ~/DLCV/Detection/Tensor_api/___new directory name____/annotations/ : wget __address__
  
  
  
  
                                                        
   <#4 Dataset을 tf.record로 변환 >
   
   -record.py download-
   
   __address__ : https://github.com/tensorflow/models/tree/master/research/object_detection/dataset_tools  /__알맞은 record.py__ (우클릭, 파일주소복사)
   
   (나중엔 우리가 record.py를 직접 customizing 해야한다..)
   
   
   
   EXPORT & PATH 설정
   
   __BASE DIR__ = ~/DLCV/Detection/Tensor_api/___new directory name___/ 여기서 진행
   
   1. export TRAIN_DIR = ~/DLCV/Detection/Tensor_api/___new directory name___
   
   2. export DATA_DIR = ~/DLCV/data/ox_pet_tensor
   
   3. export TENSOR_OBJ_DIR = ~/DLCV/Detection/Tensor_api/models/research/object_detection
   
   4. export PYTHON.PATH = $PYTHONPATH : ~/DLCV/Detection/Tensor_api/models/research : ~/DLCV/Detection/Tensor_api/models/research/object_detection
   
   5. python $TENSOR_OBJ_DIR/dataset_tools/___알맞은 record.py___ --label_map_path = $TRAIN_DIR/annotations/___알맞은 label map. pbtxt___ --data-dir = $DATA_DIR --output_dir = $TRAIN_DIR/annotations/ 
   
  
   위 1~5를 수행하면, $TRAIN_DIR/annotations/에  xxx_train.record & xxx_val.record 생성 
   
   
   
   <#5 Pipeline Config 수정 >
   
   pipeline config -> 학습을 위한 config를 일련의 파일에 모두 모아놓은 것 !
   
   
   (파일옮기기)
   
   ~/DLCV/Detection/Tensor_api/models/research/object_detection/samples/configs/___알맞은 config 파일. config___ (이거를 cp를 이용해 복사 및 이동)
   
   >> cp ___알맞은 config 파일. config___   ~DLCV/Detection/Tensor_api/____new directory name____/config/ (여기로 이동)
   
   
   
   <학습수행 코드>
   
   >> python train.py --logtostderr --train_dir = training/--pipeline_config_path =config/___알맞은 config 파일. config___
  
             위 train.py도 파일옮겨와야한다.
             
             (파일옮기기)
             
             ~/DLCV/Detection/Tensro_api/models/research/object_detection/legacy/train.py  (이거를 cp를 이용해 복사 및 이동)
             
             >> cp train.py ~/DLCV/Detection/Tensor_api/____new directory name____/ (여기로 이동)
             
   
   


  

