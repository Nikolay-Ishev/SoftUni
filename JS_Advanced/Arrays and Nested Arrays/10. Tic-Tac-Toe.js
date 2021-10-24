function tic_tac_toe(moves_arr) {
    let board = [[false, false, false],
    [false, false, false],
    [false, false, false]]

    function check_full_board(b) {
        for (let r = 0; r < 3; r++) {
            for (let c = 0; c < 3; c++) {
                if (b[r][c] == false) {
                    return false
                }
            }
        } return true
    }
    function check_free_spot(r, c) {
        if (board[r][c] != false) {
            console.log("This place is already taken. Please choose another!")
            return false
        } return true
    }
    function check_win(b) {
        // check diagonals
        if (b[0][0] != false && b[1][1] == b[0][0] && b[2][2] == b[1][1]) {
            return true
        }
        if (b[0][2] != false && b[1][1] == b[0][2] && b[2][0] == b[1][1]) {
            return true
        }
        //check rows 
        for (let i = 0; i < 3; i++) {
            if (b[i][0] != false && b[i][0] == b[i][1] && b[i][1] == b[i][2])
                return true
        }
        //check cols
        if (b[0][0] != false && b[0][0] == b[1][0] && b[0][0] == b[2][0]) {
            return true
        }
        if (b[0][1] != false && b[0][0] == b[1][1] && b[0][1] == b[2][1]) {
            return true
        }
        if (b[0][2] != false && b[0][2] == b[1][2] && b[0][2] == b[2][2]) {
            return true
        }
        return false
    }
    function change_pl(pl) {
        if (pl == "X") {
            return "O"
        }
        else { return "X" }
    }
    let player = "X"
    for (let i = 0; i < moves_arr.length; i++) {
        const cords = moves_arr[i].split(" ")
        const r = parseInt(cords[0])
        const c = parseInt(cords[1])
        if (check_free_spot(r, c) == false) {
            continue
        }
        board[r][c] = player
        if (check_win(board) == true) {
            console.log(`"Player ${player} wins!"`)
            for (let ind = 0; ind < 3; ind++) {
                console.log(board[ind].join("\t"))
            }
            return
        }
        if (check_full_board(board) == true) {
            console.log("The game ended! Nobody wins :(")
            for (let ind = 0; ind < 3; ind++) {
                console.log(board[ind].join("\t"))
            }
            return
        }
        player = change_pl(player)
    }
}


tic_tac_toe(["0 1",
"0 0",
"0 2",
"2 0",
"1 0",
"1 2",
"1 1",
"2 1",
"2 2",
"0 0"])
