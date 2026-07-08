"""
Effect size calculations.
"""

import numpy as np


class EffectSize:

    @staticmethod
    def cohens_d(a, b):

        a = np.asarray(a)

        b = np.asarray(b)

        pooled = np.sqrt(

            (

                ((len(a)-1) * np.var(a, ddof=1))

                +

                ((len(b)-1) * np.var(b, ddof=1))

            )

            /

            (len(a)+len(b)-2)

        )

        return (

            np.mean(a)

            -

            np.mean(b)

        ) / pooled

    @staticmethod
    def glass_delta(a, b):

        return (

            np.mean(a)

            -

            np.mean(b)

        ) / np.std(b, ddof=1)
