# RH15 integration checklist

- Identify the ordered model, side, revision and firmware; confirm source version and interfaces.
- Obtain matching pinout, supply/current limits, mounting drawing and safe stopping procedure.
- Confirm Linux, ROS 2 distribution, CAN adapter and all runtime dependencies. No ROS distribution compatibility is independently verified.
- Obtain licensed vendor library/header packages for the host architecture before attempting the supplied CMake build.
- Verify command units, joint indexing, limits and feedback against the device manual. Default parameters are not certified safety functions.
- Review and build in an isolated workspace; only proceed to an agreed guarded bench test after configuration review.

No ROS build, simulation or physical test has been performed by Banlumo. RY-H naming, tactile options and ROS 1 support are pending confirmation. For RH15, package naming is preserved for technical consistency rather than used to claim hardware identity.
