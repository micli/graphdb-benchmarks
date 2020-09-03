


package nebula

import (
	"fmt"
	"os"
	"os/exec"
	"strings"
)

//ImportDataToDB imports given data to db for benchmarking purpose.
func ImportDataToDB() {
	cmd := exec.Command("dgraphloader", "-r=../data/21million.rdf.gz")

	printCommand(cmd)
	output, err := cmd.CombinedOutput()
	printError(err)
	printOutput(output)
}

func printCommand(cmd *exec.Cmd) {
	fmt.Printf("==> Executing: %s\n", strings.Join(cmd.Args, " "))
}

func printError(err error) {
	if err != nil {
		os.Stderr.WriteString(fmt.Sprintf("==> Error: %s\n", err.Error()))
	}
}

func printOutput(outs []byte) {
	if len(outs) > 0 {
		fmt.Printf("==> Output: %s\n", string(outs))
	}
}
