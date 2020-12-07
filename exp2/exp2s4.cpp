#include<opencv2/opencv.hpp>
#include<iostream>
using namespace std;
using namespace cv;
int main(int a, char **p)
{
    Mat input=imread("Lena.jpg",IMREAD_GRAYSCALE);
    namedWindow("input", WINDOW_NORMAL);
    imshow("input", input);
    int w = getOptimalDFTSize(input.cols);
    int h = getOptimalDFTSize(input.rows);
    Mat padded;
    copyMakeBorder(input, padded, 0, h - input.rows, 0, w - input.cols, BORDER_CONSTANT, Scalar::all(0));
    Mat plane[] = { Mat_<float>(padded),Mat::zeros(padded.size(),CV_32F) };
    Mat complexIm;
    merge(plane, 2, complexIm);
    dft(complexIm, complexIm);
    split(complexIm, plane);
    magnitude(plane[0], plane[1], plane[0]);
    int cx = padded.cols / 2; int cy = padded.rows / 2;
    Mat temp;
    Mat part1(plane[0], Rect(0, 0, cx, cy));
    Mat part2(plane[0], Rect(cx, 0, cx, cy));
    Mat part3(plane[0], Rect(0, cy, cx, cy));
    Mat part4(plane[0], Rect(cx, cy, cx, cy)); 

    part1.copyTo(temp);
    //part4.copyTo(part1);
    temp.copyTo(part4);
    for (int i = 0; i < cx; i++)
    {
        for (int j = 0; j < cy; j++)
        {
            part1.at<int>(i, j) = 0;
        }
    }
     
    part2.copyTo(temp);
    part3.copyTo(part2);
    temp.copyTo(part3); 
     
    for (int i = 0; i < cx; i++)
    {
        for (int j = 0; j < cy; j++)
        {
            complexIm.at<int>(i, j) = 0;
        }
    }

    Mat _complexim;
    complexIm.copyTo(_complexim);
    Mat iDft[] = { Mat::zeros(plane[0].size(),CV_32F),Mat::zeros(plane[0].size(),CV_32F) };
    idft(_complexim, _complexim);
    split(_complexim, iDft); 
    magnitude(iDft[0], iDft[1], iDft[0]);
    normalize(iDft[0], iDft[0], 1, 0, NORM_MINMAX);
    namedWindow("idft", WINDOW_NORMAL);
    imshow("idft", iDft[0]);
 
    plane[0] += Scalar::all(1); 
    log(plane[0], plane[0]);
    normalize(plane[0], plane[0], 1, 0, NORM_MINMAX);
    namedWindow("dft",WINDOW_NORMAL);
    imshow("dft", plane[0]);
    waitKey(100086110);
    return 0;
}