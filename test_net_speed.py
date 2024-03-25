import speedtest

test = speedtest.Speedtest()
download_speed = test.download()
upload_speed = test.upload()

print(f"Download speed: {download_speed / 1000000:.2f} Mbps")
print(f"Upload speed: {upload_speed / 1000000:.2f} Mbps")