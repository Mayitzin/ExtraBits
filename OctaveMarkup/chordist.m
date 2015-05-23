%CHORDIST computes the chordal distance between two rotation matrices
%   d = chordist(X1) computes the chordal distance between rotation matrix
%   X1 and the identity matrix.
%
%   d = chordist(X1,X2) computes the chordal distance between rotation
%   matrices X1 and X2.
%
%   If the matrices are equal the chordal distance is zero. The matrices
%   must belong to the Special Orthogonal group in three-dimensions, that
%   is {X1,X2} belong to SO(3).
%
%   History:
%       2014.06.27. First implementation.
%
%   @author: Mario Garcia.
%   VibeWrite(c)

function d = chordist(X1,X2)

% Default values
if nargin<2
    X2 = eye(3);
end
% Check Size
if numel(X1)~=9
    error('Matrices must belong to R^(3x3)')
end
% Check Orthogonality
if det(X1*X1')~=1
    error('Matrices must belong to SO(3)')
end

% Difference of Matrices
A = X1*X2'-eye(3);

% Frobenius norm
A_F = sqrt(trace(A*A'));

% Chordal distance
d = A_F^2;