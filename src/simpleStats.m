function [ output_args ] = simpleStats(input_args )
loadFile = xlsread('oecd-countries');
histogram(loadFile)

end

