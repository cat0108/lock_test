awk -F 'cpu=|, wait_time_ns=' '
{
    # 将每行的 CPU 和等待时间存储到一个数组中
    cpu[$2] = cpu[$2] "," $3
} 
END {
    # 打印 CSV 文件头
    for (i=0; i<=7; i++) {
        if (i == 7) {
            printf "CPU%d\n", i
        } else {
            printf "CPU%d,", i
        }
    }

    # 打印每行数据，按 CPU 顺序排列
    max_samples = 0
    for (i=0; i<=7; i++) {
        split(cpu[i], times, ",")
        max_samples = (max_samples > length(times)) ? max_samples : length(times)
    }

    for (i=1; i<=max_samples; i++) {
        for (j=0; j<=7; j++) {
            split(cpu[j], times, ",")
            if (i <= length(times)) {
                printf "%s", times[i]
            } else {
                printf "0"
            }
            if (j < 7) {
                printf ","
            }
        }
        printf "\n"
    }
}
' trace.txt > output.csv
