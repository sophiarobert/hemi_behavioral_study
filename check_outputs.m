
% check key_respcorr is coded correctly

switch test_data.design(1)
    case {1,2,3,4}
        sameResp = "f";
        diffResp = "j";
    case {5,6,7,8}
        sameResp = "j";
        diffResp = "f";
end

test_data.key_respkeys = string(test_data.key_respkeys);

corr_evals = 0;
for iRow = 1:height(test_data)
    if test_data{iRow,4} == 0
        if test_data{iRow,5} == diffResp && test_data{iRow,6} == 1
            corr_evals = corr_evals + 1;
        elseif test_data{iRow,5} == sameResp && test_data{iRow,6} == 0
            corr_evals = corr_evals + 1;
        else
            disp('Diff: ' + test_data{iRow,5} + test_data{iRow,6} == 0)
        end
    elseif test_data{iRow,4} == 1
        if test_data{iRow,5} == sameResp && test_data{iRow,6} == 1
            corr_evals = corr_evals + 1;
        elseif test_data{iRow,5} == diffResp && test_data{iRow,6} == 0
            corr_evals = corr_evals + 1;
        else
            disp('Same: ' + test_data{iRow,5} + test_data{iRow,6} == 0)
        end   
    end
end

save('sophie_test2.mat', 'test_data')