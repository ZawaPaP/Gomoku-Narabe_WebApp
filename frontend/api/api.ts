import api from "@/infrastructures/axios";
import {
  CreateGameRequestType,
  UpdateGameRequestType,
  AddMoveRequestType,
} from "@/infrastructures/apiTypes";

export const createGame = async (requestData: CreateGameRequestType) => {
  try {
    const response = await api.post("/game", requestData);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const getGame = async (gameId: string) => {
  try {
    const response = await api.get(`/game/${gameId}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const updateGame = async (
  gameId: string,
  requestData: UpdateGameRequestType
) => {
  try {
    const response = await api.patch(`/games/${gameId}`, requestData);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const addMove = async (
  gameId: string,
  requestData: AddMoveRequestType
) => {
  try {
    const response = await api.post(`/add_move/${gameId}`, requestData);
    return response.data;
  } catch (error) {
    throw error;
  }
};
