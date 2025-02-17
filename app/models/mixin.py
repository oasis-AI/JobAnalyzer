from datetime import datetime

import pendulum
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column


class TimeMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        default_factory=pendulum.now,  # 可以不指明时区，但需要运行环境默认时区正确
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=pendulum.now,
        default_factory=pendulum.now,  # 可以不指明时区，但需要运行环境默认时区正确
    )
