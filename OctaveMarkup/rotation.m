%ROTATION creates a rotation matrix
%   R = rotation (ez, ey, ex, orientation) generates a DCM that
%   rotates a particle around Z, Y and X, respectively.
%
%   R = Rx(ex) * Ry(ey) * Rz(ez)
%
%   ex is the angle magnitude (in degrees) rotating around X-axis.
%   ey is the angle magnitude (in degrees) rotating around Y-axis.
%   ez is the angle magnitude (in degrees) rotating around Z-axis.
%
%   orientation defines the orientation used to construct the Rotation
%   Matrix. Possible values are strings:
%       'left' for a left-handed coordinate system.
%       'right' for a right-handed coordinate system.
%       Default value is 'right'.
%
%   Example:
%      R = rotation(10, 20, 30, 'left');
%
%   History:
%       21.01.2014. Default values for optional orientation added.
%       16.06.2014. New definitions of Rotations.
%       23.05.2015. Removed construction Rzyx = RxRyRz.
%                   Added default generation of angles in degrees.
%
%   @author: Mario Garcia.

function R = rotation(ex, ey, ez , orientation)

if nargin<4
    orientation = 'right';
end
if nargin<1
    angs = randi(180, 3, 1);
    ex = angs(1);
    ey = angs(2);
    ez = angs(3);
end

% Define Orientation of Coordinate System (Left- or Right-handed)
if strcmp(orientation, 'right')
    CS = ones(3);
elseif strcmp(orientation, 'left')
    CS = 2*eye(3)-ones(3);
else
    error('No valid orientation was given');
end

%% Rotation Matrices
% Rotation around Z-axis by angle phi
Rz = [ cosd(ez)  -sind(ez)  0;
       sind(ez)   cosd(ez)  0;
          0          0      1] .* CS;
% Rotation around Y-axis by angle theta
Ry = [ cosd(ey)  0   sind(ey);
          0      1      0    ;
      -sind(ey)  0   cosd(ey)] .* CS;
% Rotation around X-axis by angle psi
Rx = [ 1     0          0    ;
       0  cosd(ex)  -sind(ex);
       0  sind(ex)   cosd(ex)] .* CS;

%% Creation of final Rotation Matrix
R = Rz * Ry * Rx;       % <---- Rxyz