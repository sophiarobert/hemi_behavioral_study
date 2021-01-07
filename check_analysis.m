
a = load('sophie_test2.mat');
test_data = a.test_data;

CF_accuracy = 0;
CH_accuracy = 0;
FF_accuracy = 0;
FH_accuracy = 0;
CF_hits = 0;
CH_hits = 0;
FF_hits = 0;
FH_hits = 0;
CF_falses = 0;
CH_falses = 0;
FF_falses = 0;
FH_falses = 0;

trialsPerBlock = height(test_data)/4;
% signal = same, noise = diff
for iRow = 1:height(test_data)
    switch test_data{iRow,1}
        case "conf_face"
            if test_data{iRow,6} == 1
                CF_accuracy = CF_accuracy + 1;
            end
            if test_data{iRow,4} == 1 && test_data{iRow,6} == 1
                CF_hits = CF_hits + 1;
            elseif test_data{iRow,4} == 0 && test_data{iRow,6} == 0
                CF_falses = CF_falses + 1;
            else
            end
        case "conf_haus"
            if test_data{iRow,6} == 1
                CH_accuracy = CH_accuracy + 1;
            end   
            if test_data{iRow,4} == 1 && test_data{iRow,6} == 1
                CH_hits = CH_hits + 1;
            elseif test_data{iRow,4} == 0 && test_data{iRow,6} == 0
                CH_falses = CH_falses + 1;
            else
            end
        case "feat_face"
            if test_data{iRow,6} == 1
                FF_accuracy = FF_accuracy + 1;
            end
            if test_data{iRow,4} == 1 && test_data{iRow,6} == 1
                FF_hits = FF_hits + 1;
            elseif test_data{iRow,4} == 0 && test_data{iRow,6} == 0
                FF_falses = FF_falses + 1;
            else
            end
        case "feat_haus"
            if test_data{iRow,6} == 1
                FH_accuracy = FH_accuracy + 1;
            end   
            if test_data{iRow,4} == 1 && test_data{iRow,6} == 1
                FH_hits = FH_hits + 1;
            elseif test_data{iRow,4} == 0 && test_data{iRow,6} == 0
                FH_falses = FH_falses + 1;
            else
            end
    end
end

CF_accuracy = CF_accuracy/trialsPerBlock;
CH_accuracy = CH_accuracy/trialsPerBlock;
FF_accuracy = FF_accuracy/trialsPerBlock;
FH_accuracy = FH_accuracy/trialsPerBlock;

d_CF = norminv(CF_hits/(trialsPerBlock/2)) - norminv(CF_falses/(trialsPerBlock/2));
d_CH = norminv(CH_hits/(trialsPerBlock/2)) - norminv(CH_falses/(trialsPerBlock/2));
d_FF = norminv(FF_hits/(trialsPerBlock/2)) - norminv(FF_falses/(trialsPerBlock/2));
d_FH = norminv(FH_hits/(trialsPerBlock/2)) - norminv(FH_falses/(trialsPerBlock/2));

