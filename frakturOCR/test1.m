% First test
%
% Make sure you have the image package (if using Octave). Once in your local
% installation you load it with:
%
% >> pkg load image
%
% History:
%     18.08.2015. First implementation.
%
% @author: Mario Garcia
% www.mayitzin.com

%clear all
%
%disp('Starting test')
%
%I = imread('page001.png');
%I = rgb2gray(I);
[m, n] = size(I);
f1 = fspecial("unsharp", 0.1);
f2 = fspecial("unsharp", 0.9);

J1 = imfilter(I,f1);
J2 = imfilter(I,f2);
t = 200;
Ibw1 = im2bw(J1,t/256);
Ibw2 = im2bw(J2,t/256);


subplot(1,3,1)
imshow(I(800:1600,1:500));
subplot(1,3,2)
imshow(Ibw1(800:1600,1:500));
subplot(1,3,3)
imshow(Ibw2(800:1600,1:500));

%subplot(2,3,[1 4])
%imshow(I)
%subplot(2,3,[2 3])
%hist(I,256)