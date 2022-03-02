%% SM signal generation

clear
close all
clc

global xc_estim N theta0
% %NEw Data Sir USman current modulated

   
DELIMITER = ',';
HEADERLINES = 23;
%  
%Hig freq 8k new data
 A='E:\fringe_data_visualization\freqGS8000AGS0freqPS10APS20_01.csv'    % here just paste the location where you have saved the signal. remember there                                                                                                                                                                               %should b no space in the address. or any file name. 

  newData1 = importdata(A, DELIMITER, HEADERLINES);
    % Create new variables in the base workspace from those fields.
    vars = fieldnames(newData1);
    for i_local = 1:length(vars)
        assignin('base', vars{i_local}, newData1.(vars{i_local}));
    end
             

 col2 = data(:,1)';



% start = [0.1,0.7,1.3,1.9,2.5,3.1,3.7,4.3,4.9,5.5,6.1,6.7,7.3,7.9,8.5,9.1,9.4];
% End   = [0.7,1.3,1.9,2.5,3.1,3.7,4.3,4.9,5.5,6.1,6.7,7.3,7.9,8.5,9.1,9.7,10.0];
start = [0.1:0.04:9.96];
End = [0.14:0.04:10];

for i=1:length(start)
ymaxlim = max(col2(start(i)*10^4 : End(i)*10^4));
yminlim = min(col2(start(i)*10^4 : End(i)*10^4));
ymaxlim = ymaxlim + 40 * (ymaxlim/100);
yminlim = yminlim + 40 * (yminlim/100);
figure
z = plot(col2, 'Linewidth',0.7);
%%axis([-1 -0.98 -0.02 0.02])
        xlim([start(i)*10^4 End(i)*10^4]);
        ylim([yminlim ymaxlim]);
        %ylim([-13*10^-3 13*10^-3])
        name_experimental = ['Exp_signal_impulsive_one_ ',num2str(i+j-1),'.png'];
        saveas(gcf,name_experimental)
end
