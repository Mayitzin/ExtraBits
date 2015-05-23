%RANDSIG    Random Signals.
%   [R, F] = randsig(N) generates N random points of three sine-based
%   signals.
%
%   [R, F] = randsig(N, sd) generates N random points of three sine-based
%   signals with the specified covariance sd of a Normal Distribution.
%   Setting sd to zero gives a signal without noise. Default is 0.01
%       F(i) = R(i) + Normal(0,sd)
%
%   [R, F] = randsig(N, sd, sc) generates N random points with the scaling
%   factors sc, where sc is a 3-element vector with the scales for each
%   signal. Default is [1 1 1] which is equivalent to no scaling:
%       F(i) = sc(i) * (R(i) + Normal(0,sd))
%
%   R is a 3-by-N matrix that includes the random signals without noise.
%   F is a 3-by-N matrix that includes the noisy version of R.
%
%   History:
%       10.01.2014. First implementation.
%       13.01.2014. Standard deviation customization added.
%                   Scaling factors customization added.
%       27.01.2014. Fixed Sampling time.
%       23.05.2015. Added as Testing File for Octave Markup.
%
%   @author: Mario Garcia

function [R, F] = randsig(N, sd, sc)

% Standard Deviation for Gaussian Noise
if nargin<2
    sd = 0.01;
end
if nargin<3
    sc = ones(1,3);
end

% Parameters used to randomize
Freq = 100.;                % Sample Frequency
dt   = 1/Freq;              % Time-step
t    = 0:dt:(N-1)*dt;       % Times

% Create Random Sine Function in X-Axis
wx  = 1;
rnx = rand(4,1)*5;          % Random Parameters to create Sine on X
x   = sin((rnx(1)).*wx*t).*sin(wx*t);   % Real signal in X
% Add disturbances to signal
ax  = sc(1);                % Scaling
bx  = 0;                    % Bias
nx  = sd*randn(size(x));
X   = ax * (x + nx + bx);   % Noisy signal in X

% Create Random Sine Function in Y-Axis
wy  = 1;
rny = rand(4,1)*5;          % Random Parameters to create Sine on Y
y   = sin((rny(1)).*wy*t).*sin(wy*t);   % Real signal in Y
% Add disturbances to signal
ay  = sc(2);                % Scaling
by  = 0;                    % Bias
ny  = sd*randn(size(y));
Y   = ay * (y + ny + by);   % Noisy signal in Y

% Create Random Sine Function in Z-Axis
wz  = 1;
rnz = rand(4,1)*3;          % Random Parameters to create Sine on Z
z   = sin((rnz(1)).*wz*t).*sin(wz*t);   % Real signal in Z
% Add disturbances to signal
az  = sc(3);                % Scaling
bz  = 0;                    % Bias
nz  = sd*randn(size(z));
Z   = az * (z + nz + bz);   % Noisy signal in Z

% Signals
R = [x; y; z];      % Real Signal
F = [X; Y; Z];      % Noisy Signal