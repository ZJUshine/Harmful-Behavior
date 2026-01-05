#!/bin/bash

set -e

# path config
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HARMFUL_JSON="${SCRIPT_DIR}/harmful_instances.json"
CINEMATIC_RECORDER="${SCRIPT_DIR}/tools/cinematic_recorder.py"
VIDEO_OUTPUT_DIR="${SCRIPT_DIR}/harmful_videos"

# create output directory
mkdir -p "$VIDEO_OUTPUT_DIR"

# check mapped tasks file
MAPPED_TASKS_FILE="${SCRIPT_DIR}/tasks.txt"

# read mapped tasks list
instructions=$(cat "$MAPPED_TASKS_FILE")


# process each task
total_tasks=$(echo "$instructions" | wc -l)
current_task=0
success_count=0
fail_count=0
skip_count=0

# create log file
log_file="${VIDEO_OUTPUT_DIR}/generation_log.txt"
error_log="${VIDEO_OUTPUT_DIR}/error_log.txt"
echo "Video generation log - $(date)" > "$log_file"
echo "Error log - $(date)" > "$error_log"

echo "$instructions" | while read -r task_name; do
    if [ -z "$task_name" ]; then
        continue
    fi
    
    current_task=$((current_task + 1))
    echo "[$current_task/$total_tasks] Processing task: $task_name"
    
    # check if the corresponding Python task file exists
    task_file="${SCRIPT_DIR}/rlbench/tasks/${task_name}.py"
    if [ ! -f "$task_file" ]; then
        echo "  警告: Task file not found: $task_file，跳过..." | tee -a "$error_log"
        echo "  警告: Task file not found: $task_file, skipping..." | tee -a "$error_log"
        skip_count=$((skip_count + 1))
        continue
    fi
    
    # generate video
    video_path="${VIDEO_OUTPUT_DIR}/${task_name}.mp4"
    if [ -f "$video_path" ]; then
        echo "  视频已存在，跳过: $video_path" | tee -a "$log_file"
        echo "  Video already exists, skipping: $video_path" | tee -a "$log_file"
        skip_count=$((skip_count + 1))
        continue
    fi
    
    echo "  正在生成视频..." | tee -a "$log_file"
    echo "  Generating video..." | tee -a "$log_file"
    
    # call cinematic_recorder.py to generate video
    if python3 "$CINEMATIC_RECORDER" \
        --save_dir="$VIDEO_OUTPUT_DIR" \
        --tasks="$task_name">>"$error_log"; then
        
        echo "  ✓ 视频生成成功: $video_path" | tee -a "$log_file"
        echo "  ✓ 视频生成成功: $video_path" | tee -a "$log_file"
        success_count=$((success_count + 1))
    else
        echo "  ✗ 错误: 生成视频失败: $task_name" | tee -a "$error_log"
        echo "  ✗ 错误: 生成视频失败: $task_name" | tee -a "$error_log"
        fail_count=$((fail_count + 1))
    fi
    
    # show progress
    echo "  进度: 成功=$success_count, 失败=$fail_count, 跳过=$skip_count"
    echo "  Progress: success=$success_count, fail=$fail_count, skip=$skip_count"
done

# show final statistics
echo "======== Video generation completed ========"
echo "Total tasks: $total_tasks"
echo "Successfully generated: $success_count"
echo "Failed: $fail_count"  
echo "Skipped tasks: $skip_count"
echo "Log file: $log_file"
echo "Error log: $error_log"

echo "All videos generated successfully!"
echo "Output directory: $VIDEO_OUTPUT_DIR"
