% -----------------------------------------------------------------------------
%
% -----------------------------------------------------------------------------

% Synthetic input data
data = [0, 1, 2, 3, 4, 5, 6, 7, 8]

% ...
rsize = size(data, 2);
dimSize = sqrt(rsize);
arr = zeros(dimSize, dimSize);

% ...
for col = 1:dimSize
  values = data((col - 1) * dimSize + 1: col * dimSize);
  arr(:, col) = values;
end

% ...
[v, d] = eig(arr)

% Console Output
% --------------
%
% data =
% 
%    0   1   2   3   4   5   6   7   8
% 
% v =
% 
%    0.44024   0.89788   0.40825
%    0.56787   0.27843  -0.81650
%    0.69549  -0.34101   0.40825
% 
% d =
% 
% Diagonal Matrix
% 
%    1.3348e+01            0            0
%             0  -1.3485e+00            0
%             0            0  -9.9918e-16
%
%