from model import *
from data import *
import os
import warnings
import keras
warnings.filterwarnings("ignore")
os.environ["CUDA_VISIBLE_DEVICES"] = "0"



if __name__ == '__main__':

    #ѵ����������·��
    train_path = "./data/train"
    image_folder = "image"
    label_folder = "annotation"

    #��������ָ��ͼ��·��
    test_path = "./data/crack/test_new"

    #��������ָ�����·��
    save_path = "./data/crack/test_new"

    #
    dp = data_preprocess(train_path,image_folder,label_folder,test_path,save_path)

    # tbCallBack = keras.callbacks.TensorBoard(log_dir='./log',
    #                                          histogram_freq=1,
    #                                          write_graph=True,
    #                                          write_images=True)

    # ѵ��ģ��
    train_data = dp.trainGenerator(batch_size=2)

    model = unet()

    #����ѵ���Ļ����������滻�������м��ɣ�����ѵ�������ݲ�Ҫ��ԭ�������ݷŵ�һ�𣬵�����һ���ļ��У�
    # Ȼ��train_path��image_folder��label_folder��Ϊ�������ݵ��ļ�·��
    # model = load_model('./my_model_0228.hdf5')

    model_checkpoint = keras.callbacks.ModelCheckpoint('./model/crack_model.hdf5', monitor='loss',verbose=1,save_best_only=True)
    #��ʼѵ��ģ�ͣ�������10�֣�ÿ��500��
    model.fit_generator(train_data,steps_per_epoch=500,epochs=20,callbacks=[model_checkpoint])

