// apiTypes.ts

export interface CreateGameRequestType {
  player: string;
  boardSize: number;
}

export interface UpdateGameRequestType {
  status: string;
}

export interface AddMoveRequestType {
  row: number;
  column: number;
}
