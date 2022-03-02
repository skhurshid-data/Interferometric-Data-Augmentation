%% SM signal generation

clear all
close all
clc

C = 1:1:4;
%C = 10:1:35;
%C = 0.1:0.1:1;
%C = 0:0.2:1;
%K = 1:0.2:5;
K = 5;
for i = 1:length(C)

    for j = 1:length(K)
        phi = pi/2;
        alpha = 5;
        amp = 2.1;   % Peak to peak Vibration Amp in terms of No of Lambda
    %     K = 5;


        frequency = 3;    % Freq in Hz
        sampling_f = 11*1e3;  % X samples per sec
        dt = 1/sampling_f;



        %M=1e7;      % total no of acquisition points
        time_in_sec = 1;
        M = sampling_f*time_in_sec;     % total no of acquisition points

        time = [0:dt:time_in_sec]';
        time = time(1:end-1);

        ramp_ON = 0;
        if ramp_ON == 1

            ramp = zeros(M,1);
            samples_per_period = (sampling_f)/frequency;
            samples_per_half_period = samples_per_period/2;

            ramp_pos = [-1:1/samples_per_half_period*2 :1]';
            ramp_neg = [1:-1/samples_per_half_period*2 :-1]';
            ramp_unit = [ ramp_pos(1:end-1) ; ramp_neg(1:end-1)];

            %     figure('name','double vvv  ')
            %     plot(ramp_unit)


            for i = 1:1:round(M/samples_per_period)
                ramp( (i-1)*samples_per_period + 1: i*samples_per_period,1) = ramp_unit;
            end

            %     figure('name','double vvv  ')
            %     plot(ramp)

            Displ = 2*pi*amp*ramp;  %

        else

            % 7.4nm err
               Displ = 2*pi*amp*(sin(2*pi*((1/M)*frequency*(dt*M))*[0:M-1] + pi/2) )';  %
               Displ = Displ + 2*pi*(amp/1)*(sin(2*pi*((1/M)*(frequency*1.5)*(dt*M))*[0:M-1] + 0*pi/8) )';  %
               Displ = Displ + 2*pi*(amp/1)*(sin(2*pi*((1/M)*(frequency*2.5)*(dt*M))*[0:M-1] + 5*pi/4) )';  %
               Displ = Displ + 2*pi*(amp/1)*(sin(2*pi*((1/M)*(frequency*3)*(dt*M))*[0:M-1] + pi/4) )';  %
               Displ = Displ + 2*pi*(amp/1)*(sin(2*pi*((1/M)*(frequency*5.5)*(dt*M))*[0:M-1] + 3*pi/4) )';  %

         %   Displ = 2*pi*amp*(sin(2*pi*((1/M)*frequency*(dt*M))*[0:M-1] + pi/2) )';  %

        end



        xs_sim = K(j)*pi - atan(alpha) + Displ + phi;

        N = length(xs_sim);


        xc_sim = xc_fonction_xs_interpol_f_xs(xs_sim,C(i),atan(alpha));


        P_simo = cos(xc_sim); % original noise-less SM signal


        %% Amp Modulation of SM signal
        % V_upper = 1;
        % V_lower = 0.1;
        % mod = (V_upper:-(V_upper-V_lower)/(1*N):V_lower)';
        % mod = mod(1:end-1);
        %
        % P_sim2 = P_sim.*mod;


        %% Addition of AWGN
        Noise = 0.10*randn(length(P_simo),1);
        %Noise = 0.15*randn(length(P_simo),1);
        %Noise = 0.23*randn(length(P_simo),1);
        P_x_signal = rms(P_simo);    % SNR
        P_x_noise = rms(Noise);     % SNR
        SNR = P_x_signal/P_x_noise      % SNR
        SNR_db= 2*10 * log10(SNR)         % SNR in db

        P_sim = P_simo + Noise;         % noise addition



        lambda = 0.785; % in micro-meter
        Displ = Displ* (lambda/(4*pi));

    %     figure('name',['For C = ', num2str(C(i))])
% % % % %         figure('units','normalized','outerposition',[0 0 1 1])
% % % % %         plot(time,P_simo,'LineWidth',3),grid off
% % % % %         xlabel('Time (s)')
% % % % %         ylabel('Amp. (au)')
% % % % %         %legend (['Noise-less LDOOP SM signal with C = ',num2str(C(i)),'& K = ',num2str(K(j))])
% % % % %         xlim([0.88 1.0])
% % % % %         ylim([-1.6 1.6])

% % % % %         name_Noise_less = ['Noise-less_LDOOP_SM_signal ',num2str(i+j-1),'.png'];
% % % % %         saveas(gcf,name_Noise_less);
    %     pause();
% % % % %         close
    %     subplot(3,1,1); plot(time,Displ),grid on
    %     legend ('Target Vibration')
    %     xlabel('Time (s)')
    %     ylabel('Amp. (µm)')

    %     figure('name',['For C = ', num2str(C(i))]) noisy plot starts here
        %figure('units','normalized','outerposition',[0 0 1 1])
        figure
        plot(time,P_sim,'LineWidth',1),grid off

        f = gca;
        xlabel('Time (s)');
        ylabel('Amp. (au)');
        f.FontWeight = 'bold';
        f.FontSize = 20;
        f.LineWidth = 4;
        %legend (['Noisy LDOOP SM signal with C = ',num2str(C(i)),'& K = ',num2str(K(j))])
        xlim([0.73 0.80])
        ylim([-2 2])

        name_Noise_less = ['Noise-less_LDOOP_SM_signal ',num2str(i+j-1),'.png'];
        exportgraphics(gcf,name_Noise_less, 'Resolution',600)
% % % % %         name_Noisy = ['Noisy_LDOOP_SM_signal ',num2str(i+j-1),'.png'];
% % % % %         saveas(gcf,name_Noisy)
    %     pause();
        close
    %     subplot(3,1,1); plot(time,Displ),grid on
    %     legend ('Target Vibration')
    %     xlabel('Time (s)')
    %     ylabel('Amp. (µm)')

        %% TRANS DETECTION

        % % P = P_sim;
        % % 
        % % %N = length(P);
        % % seuil_pos = 0.554
        % % seuil_neg = 0.554
        % % 
        % % %P = filtfilt(ones(15,1)/15,1,P);
        % % %P_org = filtfilt(ones(15,1)/15,1,P_org);
        % % 
        % % 
        % % chopped = 50;
        % % [trans,ac,P_norm] = static_trans_detection( P, seuil_pos,seuil_neg,chopped );
        % % 
        % % N = length(trans);
        % % 
        % % figure('name','p and trans')
        % % plot((1:N),trans*max(P)*2,'r',(1:N),P,'b'),grid on
        % % xlabel ('p  ')
        % % legend('trans','P')
        % % ylabel('Amplitude')
    end
end