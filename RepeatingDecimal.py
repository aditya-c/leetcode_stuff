class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # get sign
        boolean_sign = numerator > 0 and denominator > 0
        sign = ""
        orig_numerator = numerator
        if not boolean_sign:
            sign = "-"

        # get integer part
        integral = 0
        if abs(numerator) >= abs(denominator):
            integral = self.get_integral(numerator, denominator)
        # the decimal part
        decimalMap = {}
        is_repeated = False
        decimal = self.get_decimal(numerator, denominator)

        counter = 0
        while float(decimal) != 0.0 and counter < 9:  # using 9 bit precision
            counter += 1
            if decimal in decimalMap:
                is_repeated = True
                decimalMap[decimal] = self.get_integral(numerator, denominator)
                break
            else:
                decimalMap[decimal] = self.get_integral(numerator, denominator)
                numerator *= 10
                decimal = self.get_decimal(numerator, denominator)

        decimalStr = None

        if is_repeated:
            decimalStr = "({})".format(decimalMap[decimal])
        else:
            if orig_numerator % denominator > 0:
                decimalStr = str((float(orig_numerator) / denominator) % 1)[2:]

        if decimalStr:
            result = "".join([sign, str(integral), ".", decimalStr])
        else:
            result = "".join([sign, str(integral)])
        return result

    def get_decimal(self, numerator, denominator):
        result = "{0:.9f}".format((float(numerator) / denominator) % 1)
        return result   # using 9 bit precision

    def get_integral(self, numerator, denominator):
        return abs(numerator) // abs(denominator)


test = Solution()
print(test.fractionToDecimal(1, 6))
