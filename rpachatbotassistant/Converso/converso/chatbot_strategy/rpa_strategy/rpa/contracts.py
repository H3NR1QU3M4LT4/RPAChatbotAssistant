from dataclasses import dataclass


@dataclass
class User:
    name: str
    phone_number: str


@dataclass
class NIBRequestObject:
    user: User
    intention: str
    nib_iban: str


@dataclass
class ParkingLotRequestObject:
    user: User
    intention: str
    date: str
    office_location: str
    parking_lot: str


@dataclass
class TimeOffRequestObject:
    user: User
    intention: str
    date: str


@dataclass
class RoomTableOfficeRequestObject:
    user: User
    intention: str
    date: str
    office_location: str
    table_room_office: str
