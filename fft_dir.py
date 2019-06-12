import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import keras
import librosa
import csv

sampling_rate = 16000
raw_sounds = []
wav_file_names = []
arr = []
fft_size = 16000
stft_matrix_size = 1 + fft_size // 2

f = open('output_06.csv', 'a') # csvファイルを作成
writer = csv.writer(f, lineterminator='\n')
csvlist = []


def main():

    data_dir_path = u"./2018_11_15/06" #wavファイルのあるディレクトを指定
    file_list = os.listdir(r'./2018_11_15/06')

    for file_name in file_list:
        root, ext = os.path.splitext(file_name)

        if ext == u'.wav':
            abs_name = data_dir_path + '/' + file_name

            for wav_file_name in sorted(glob.glob(abs_name)):
                data, sample_rate = librosa.load(
                wav_file_name, sr=sampling_rate, duration=30)
                print('{} ({} Hz) '.format(wav_file_name, sample_rate))
                raw_sounds.append(data)
                wav_file_names.append(wav_file_name)
                f.write(root)

            X = np.empty((0, stft_matrix_size))
            y = np.empty(0)

            for i, wav_file_name in enumerate(wav_file_names):
                d = np.abs(librosa.stft(raw_sounds[i], n_fft=fft_size, window='hamming'))
                X = np.vstack([X, d.transpose()])
                y = np.hstack([y, [i] * d.shape[i]])
                a  = librosa.fft_frequencies(sr=sampling_rate, n_fft=fft_size)
                b = np.mean(d, axis=1)
                c = np.where(a <= 5000)
                d = np.where(a >= 8000)
                b[c] = 0
                b[d] = 0
                ax = plt.subplot()
                ax.set_xlim([0, 16000])
                ax.set_ylim([0, 20])
                plt.plot(a,b)
                flag = np.where(b > 4.0, 1, 0)
                if flag.max() != 0:
                    print("1")
                    arr.append(1)
                    f.write(",1\n")
                else:
                    print("0")
                    arr.append(0)
                    f.write(",0\n")
                wav_file_names.pop(-1)
                raw_sounds.pop()

if __name__ == '__main__':
    main()
    print(arr)
    f.close()
