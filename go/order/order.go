package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

// 定义需要监控 Counter 类型对象
var (
	opsProcessed = promauto.NewCounterVec(prometheus.CounterOpts{
		Name: "order_service_processed_orders_total",
		Help: "The total number of processed orders",
	}, []string{"status"}) // 处理状态
)

// 订单处理
func makeOrder(w http.ResponseWriter, r *http.Request) {
	fmt.Println("makeOrder:333")
	opsProcessed.WithLabelValues("success").Inc() // 成功状态
	// opsProcessed.WithLabelValues("fail").Inc() // 失败状态

	// 下单的业务逻辑
}

func main() {
	// 暴露自定义的指标
	fmt.Println("222")
	mx := http.NewServeMux()
	mx.Handle("/metrics", promhttp.Handler())
	go http.ListenAndServe(":8080", mx) //注意这里，不开协程直接就监听阻塞了

	// 启动web服务器
	mt := http.NewServeMux()
	mt.HandleFunc("/", makeOrder) // 设置访问的路由
	fmt.Println("启动")
	err := http.ListenAndServe(":9090", mt) // 设置监听的端口
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}
