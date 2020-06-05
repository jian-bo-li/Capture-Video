import os
import cv2
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--video', type=str, default='video.flv')
    parser.add_argument('-p', '--path', type=str, default='./pic')
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    if not os.path.exists(args.path):
        os.makedirs(args.path)
    capture = cv2.VideoCapture(args.video)
    count = 0
    while True:
        success, frame = capture.read()
        if not success:
            break
        output = os.path.join(args.path, '{}.jpg'.format(count))
        cv2.imwrite(output, frame)
        count += 1
        print('No. {} captured. Saved to {}'.format(count, output))

if __name__ == '__main__':
    main()
