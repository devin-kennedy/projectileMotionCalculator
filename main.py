from motionCalculator import Motion


def main():
    calculator = Motion(
        theta=45,
        vi=15
    )
    calculator.plot()


if __name__ == "__main__":
    main()
