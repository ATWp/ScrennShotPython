package main
import (
    "fmt"
	"bufio"
    "io"
	"os/exec"
)

func copyOutput(r io.Reader) {
    scanner := bufio.NewScanner(r)
    for scanner.Scan() {
        fmt.Println(scanner.Text())
    }
}

func Start_py(){
	cmd := exec.Command("python", "screnDoings.py")
    stdout, err := cmd.StdoutPipe()
    if err != nil {
        panic(err)
    }
	
    stderr, err := cmd.StderrPipe()
    if err != nil {
        panic(err)
    }
	
    err = cmd.Start()
    if err != nil {
        panic(err)
    }

    go copyOutput(stdout)
    go copyOutput(stderr)
    cmd.Wait()
}


func main() {

	Start_py()
	fmt.Print("Press 'Alt' to doings screenshot...")
	fmt.Print("Press 'Ctrl + Q' to close...")
    fmt.Scanln()
}