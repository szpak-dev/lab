#!/usr/bin/env python3
import argparse
import rows as rows
import script_runner as sr


def script(filename):
    sr.run_script(filename)


def init():
    print("Running initiating scripts...\n")
    script('1.1-create-database')
    script('1.2-create-schema')
    script('1.3-create-tables')


def insert_initial_data():
    script('2.1-insert-cars')
    script('3.1-insert-clients')
    script('3.2-insert-rentals')


def reset():
    print("Dropping and recreating Tables...\n")
    script('1.4-drop-tables')
    script('1.3-create-tables')


def load_fake_clients(num):
    print("Feeding database with fake clients...\n")
    reset()
    rows.insert_clients(num)


def load_fake_cars(num):
    pass


parser = argparse.ArgumentParser()
parser.add_argument('--init', type=int, default=0, help='Start with installing Rentals DB')
parser.add_argument('--data', type=int, default=0, help='Add initial data form Tutorial')
parser.add_argument('--reset', type=int, default=0, help='Number of cars to insert')
parser.add_argument('--clients', type=int, default=0, help='Number of clients to insert')
parser.add_argument('--cars', type=int, default=0, help='Number of cars to insert')
args = parser.parse_args()

if args.init > 0:
    init()

elif args.data > 0:
    insert_initial_data()

elif args.reset > 0:
    reset()

elif args.clients > 0:
    load_fake_clients(args.clients)

print(args)
