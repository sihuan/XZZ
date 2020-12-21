package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os/exec"
)

func checkErr(err error) {
	if err != nil {
		fmt.Println(err)
	}
}

func handleStatus(writer http.ResponseWriter, request *http.Request) {
	cmd := exec.Command("papermc", "status")
	var out bytes.Buffer
	cmd.Stdout = &out
	err := cmd.Run()
	if err != nil {
		fmt.Fprintf(writer, "Error")
		return
	}
	fmt.Fprintf(writer, out.String())
}

func handleList(writer http.ResponseWriter, request *http.Request) {
	cmd := exec.Command("papermc", "command", "list")
	var out bytes.Buffer
	cmd.Stdout = &out
	err := cmd.Run()
	if err != nil {
		fmt.Fprintf(writer, "Error")
		return
	}
	fmt.Fprintf(writer, out.String())
}

func handleSay(writer http.ResponseWriter, request *http.Request) {
	saywhat, _ := ioutil.ReadAll(request.Body)
	cmd := exec.Command("papermc", "command", "say", string(saywhat))
	var out bytes.Buffer
	cmd.Stdout = &out
	err := cmd.Run()
	if err != nil {
		fmt.Fprintf(writer, "Error")
		return
	}
	fmt.Fprintf(writer, "0")
}

func main() {
	http.HandleFunc("/status", handleStatus)
	http.HandleFunc("/list", handleList)
	http.HandleFunc("/say", handleSay)
	fmt.Println("Running at port 58941 ...")
	err := http.ListenAndServe("172.26.66.2:58941", nil)
	if err != nil {
		log.Fatal("ListenAndServe: ", err.Error())
	}
}
