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

% clear all
% 
% disp('Starting test')
% 
% I = imread('page001.png');
% I = rgb2gray(I);
% [m, n] = size(I);
% 
% % Sharpening Filters
% f1 = fspecial('unsharp', 0.1);
% f2 = fspecial('unsharp', 0.9);
% 
% % Sharped Images
% J1 = imfilter(I,f1);
% J2 = imfilter(I,f2);
% 
% % Binarized Images
% t = 220;
% Ibw1 = im2bw(J1,t/256);
% Ibw2 = im2bw(J2,t/256);

% Dilate image vertically
se2 = strel('square',5);
Idi2 = ~imdilate(~Ibw2,se2);

% Centroids
Ics2 = regionprops(~Idi2,'centroid');
cs2 = cat(1, Ics2.Centroid);

% Pseudo-Histograms
x = sum(~Ibw2,2);
y = zeros(m);
for i = 1:m
    y(i) = sum(find(round(cs2(:,2))==i));
end

% Plotting Images
figure()
subplot(1,4,1)
    imshow(I);
subplot(1,4,2)
    imshow(Idi2); hold on
    plot(cs2(:,1),cs2(:,2), 'r*'); hold off
subplot(1,4,3) % Histogram of Pixels
    plot(gca, 1:m,x, 'r-')
    set(gca,'view',[90 90])
subplot(1,4,4) % Histogram of Points
    plot(gca, 1:m,y, 'r-')
    set(gca,'view',[90 90])

